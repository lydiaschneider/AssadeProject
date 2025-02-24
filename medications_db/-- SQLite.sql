-- SQLite
SELECT * FROM medications;

SELECT med_id, name, stock_levels FROM medications WHERE stock_levels IS NULL;

UPDATE medications SET stock_levels = 0 WHERE stock_levels IS NULL;

UPDATE medications SET stock_levels = ? WHERE med_id = ?

