DECLARE 

    test_values INT NOT NULL DEFAULT 1; 

BEGIN

    FOR i IN 1..test_values LOOP

      INSERT INTO human_season(human_name_fk,season_year_fk)

            VALUES ('Paco Bienzobas' ,1934); 
            
      INSERT INTO human_season(human_name_fk,season_year_fk)

            VALUES ('Manuel Olivares',1935); 
               
    END LOOP;

END;


