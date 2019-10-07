SELECT 
    f.id AS 'Farmer Id',
    f.farmer_name AS 'Farmer Name',
    f.gender AS 'Gender',
    f.dob AS 'DOB',
    p.name AS 'Product Name',
    cc.country_name AS 'Country Name',
    rg.region_name AS 'Region Name',
    dt.district_name AS 'District Name',
    pl.place_name AS 'Place Name',
    fg.name AS 'Farmer Group Name',
    pt.name AS 'Partner Name',
    pg.name AS 'Programmer Name',
    sc.name AS 'Section Name',
    em.enumerator_name AS 'Enumerator Name',
    sb.submission_date AS 'Submitted On',
    sb.id AS 'Survey Id',
    md.name AS 'Module Name'
FROM
    farmer.farmer f
        JOIN
    master.farmergroups fg ON fg.farmer_group_id = f.farmer_group_id
        RIGHT JOIN
    survey.submittedmodules sb ON sb.farmer_id = f.id
        RIGHT JOIN
    survey.modules md ON md.id = sb.module_id
        RIGHT JOIN
    master.enumerator em ON em.enumerator_id = f.enumerator_id
        RIGHT JOIN
    master.products p ON p.id = fg.product_id
        RIGHT JOIN
    master.country cc ON cc.country_id = f.country_id
        RIGHT JOIN
    master.region rg ON rg.region_id = f.region_id
        RIGHT JOIN
    master.district dt ON dt.district_id = f.district_id
        RIGHT JOIN
    master.place pl ON pl.place_id = f.place_id
        RIGHT JOIN
    master.partners pt ON pt.partners_id = fg.partner_id
        RIGHT JOIN
    master.programmes pg ON pg.id = fg.programme_id
        RIGHT JOIN
    master.sections sc ON sc.id = f.section_id
WHERE
    f.farmer_name IN (SELECT 
            fm.farmer_name
        FROM
            farmer.farmer fm
                JOIN
            master.farmergroups fg ON fg.farmer_group_id = fm.farmer_group_id
        WHERE
            TRIM(fm.farmer_name) != ''
                AND fm.app_id = 1
                AND fg.app_id = 1
        GROUP BY fm.farmer_name , fm.dob, fg.product_id, fm.country_id, fm.farmer_group_id, fm.region_id, fm.district_id, fm.place_id, fg.partner_id, fg.programme_id, fm.section_id
        HAVING COUNT(fm.id) > 1)
        AND f.app_id = 1
        AND fg.app_id = 1
ORDER BY f.farmer_name;