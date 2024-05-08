-- common table expressions for origin or destination that refers to itself in the inner join (recursion)
-- to select all ports within a region
-- if the input slug/id is a port, the Union with Ports will fill the temporary table
-- with a single entry, the port ID
-- it is assumed that port and region id's are always distinct, and that a port only ever
-- has a region as parent.

WITH RECURSIVE OriginRegionsOrPorts AS (
    SELECT slug, name, parent_slug
    FROM Regions
    WHERE slug = %(origin_slug)s
    UNION
    SELECT code, name, parent_slug
    FROM Ports
    WHERE code =  %(origin_slug)s
  UNION ALL
    SELECT r.slug, r.name, r.parent_slug
    FROM Regions r
    INNER JOIN OriginRegionsOrPorts ors ON r.parent_slug = ors.slug
),
DestinationRegionsOrPorts AS (
    SELECT slug, name, parent_slug
    FROM Regions
    WHERE slug = %(destination_slug)s
    UNION
    SELECT code, name, parent_slug
    FROM Ports
    WHERE code = %(destination_slug)s
  UNION ALL
    SELECT r.slug, r.name, r.parent_slug
    FROM Regions r
    INNER JOIN DestinationRegionsOrPorts drs ON r.parent_slug = drs.slug
),
OriginPorts AS (
    SELECT code
    FROM Ports
    WHERE parent_slug IN (SELECT slug FROM OriginRegionsOrPorts)
    UNION
    SELECT code
    FROM Ports
    WHERE code = %(origin_slug)s
),
DestinationPorts AS (
    SELECT code
    FROM Ports
    WHERE parent_slug IN (SELECT slug FROM DestinationRegionsOrPorts)
    UNION
    SELECT code
    FROM Ports
    WHERE code =  %(destination_slug)s
),
DateSeries AS (
    SELECT generate_series(%(start_date)s::date, %(end_date)s::date, interval '1 day')::date AS day
)
SELECT ds.day,
       CASE WHEN COUNT(pr.price) >= 3 THEN ROUND(AVG(pr.price), 2) ELSE NULL END AS average_price
FROM DateSeries ds
LEFT JOIN Prices pr
  ON pr.day = ds.day
  AND pr.orig_code IN (SELECT code FROM OriginPorts)
  AND pr.dest_code IN (SELECT code FROM DestinationPorts)
GROUP BY ds.day
ORDER BY ds.day;