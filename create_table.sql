CREATE TABLE playerdata (
    id SERIAL PRIMARY KEY,
    Player varchar NOT NULL,
    Season varchar(5),
    AGE real,
    G real,
    GS real,
    MP real,
    FG real, 
    FGA real, 
    FGP real, 
    "3p" real,
    "3pa" real,
    "3pp" real, 
    "2p" real, 
    "2pa" real, 
    "2pp" real, 
    eFGP real, 
    FT real, 
    FTA real, 
    FTP real, 
    ORB real,
    DRB real, 
    TRB real, 
    AST real, 
    STL real, 
    BLK real, 
    TOV real, 
    PF real, 
    PSG real
);

COPY playerdata (player, season, age, g, gs, mp, fg, fga, fgp, "3p", "3pa", "3pp", "2p", "2pa", "2pp", efgp, ft, fta, ftp, orb, drb, trb, ast, stl, blk, tov, pf, psg) FROM '/Users/andric/Documents/workspace/aut_vincere/aut_vincere_multiyear_trimmeddat.csv' WITH DELIMITER ',' CSV HEADER;

