drop table factura_a;
drop table aprovizionare;
drop table producator;
drop table factura_c;
drop table cosmetice;
drop table comanda;
drop table angajat;
drop table transport;

drop database DEPOZIT;


CREATE DATABASE DEPOZIT;
USE DEPOZIT;

CREATE TABLE producator 
    ( CUI     	   DECIMAL(8,0)  
    , denumire     VARCHAR(35)	NOT NULL  UNIQUE
    , brand 	   VARCHAR(25)	 NOT NULL 
    , localitate   VARCHAR(25)	  NOT NULL
    , strada 	   VARCHAR(25)		
    , CONSTRAINT     prod_CUI_PK  PRIMARY KEY (CUI) 
    ); 
    

CREATE TABLE aprovizionare
    ( nr_comanda_a     DECIMAL(6,0)   
    , CUI		   	   DECIMAL(8,0)	NOT NULL 
    , data_primire	   DATE			NOT NULL
	);

ALTER TABLE aprovizionare  
ADD (  
     CONSTRAINT     apr_NR_PK  PRIMARY KEY (nr_comanda_a) 
	, CONSTRAINT FK_Aprovizionare
	  FOREIGN KEY (CUI) REFERENCES producator(CUI) ON DELETE CASCADE ON UPDATE CASCADE			
    ); 


CREATE TABLE cosmetice
    ( id_produs			DECIMAL(4,0)   
    , nume	   	        VARCHAR(25)  NOT NULL
    , categorie			VARCHAR(25)
    , stoc				DECIMAL(4,0)
    , pret_unit		    DECIMAL(6,2)  NOT NULL
    , data_expirare		DATE          NOT NULL
    );
    
ALTER TABLE cosmetice 
ADD (    
      CONSTRAINT     id_PK  PRIMARY KEY (id_produs, pret_unit) 
    , CONSTRAINT     pret_const_cosm
                     CHECK     (pret_unit > 0)
    );
 
 
 CREATE TABLE factura_a
    ( nr_crt_a 			DECIMAL(3,0)
    , nr_comanda_a      DECIMAL(6,0)  NOT NULL 
    , id_produs 		DECIMAL(4,0)  
    , cantitate			DECIMAL(4,0)  NOT NULL 
    , pret_unit			DECIMAL(6,2) 
    
    , CONSTRAINT     fact_a_PK  PRIMARY KEY (nr_crt_a) 
    ); 

    
ALTER TABLE factura_a
ADD (
	CONSTRAINT FK_Fact_A_nr
	FOREIGN KEY (nr_comanda_a) REFERENCES aprovizionare(nr_comanda_a) ON DELETE CASCADE ON UPDATE CASCADE,
	CONSTRAINT FK_Fact_A_id_pret
	FOREIGN KEY (id_produs, pret_unit) REFERENCES cosmetice(id_produs, pret_unit) ON DELETE SET NULL,
	CONSTRAINT check_fact_A_cantitate
    CHECK (cantitate > 0)
    );
 

CREATE TABLE comanda
    ( nr_comanda_c      DECIMAL(6,0)  
    , data_plasare	   	DATE  		NOT NULL
    , data_expediere	DATE 		
    , id_magazin		DECIMAL(4,0) NOT NULL 
    , nr_masina			VARCHAR(7)	  NOT NULL
    , id_angajat		DECIMAL(4,0)  NOT NULL
    );
    
    
ALTER TABLE comanda
ADD (    
      CONSTRAINT     nr_com_PK  PRIMARY KEY (nr_comanda_c) ,
      CONSTRAINT     check_data
      CHECK    (data_plasare <= data_expediere)
    );


CREATE TABLE factura_c
    ( nr_crt_c 			DECIMAL(3,0)
    , nr_comanda_c      DECIMAL(6,0)  NOT NULL 
    , id_produs 		DECIMAL(4,0)   
	, cantitate			DECIMAL(4,0)  NOT NULL 
    , pret_unit			DECIMAL(6,2)
    
    , CONSTRAINT     fact_c_PK  PRIMARY KEY (nr_crt_c) 
    ); 

    
ALTER TABLE factura_c
ADD ( 
	CONSTRAINT FK_Fact_C_id_pret
	FOREIGN KEY (id_produs, pret_unit) REFERENCES cosmetice(id_produs, pret_unit) ON DELETE SET NULL,
	CONSTRAINT FK_Fact_C_nr
	FOREIGN KEY (nr_comanda_c) REFERENCES comanda(nr_comanda_c) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT check_fact_C_cantitate
    CHECK (cantitate > 0)
	);   


CREATE TABLE angajat
	( id_angajat 		DECIMAL(4,0) 	
    , nume				VARCHAR(25) NOT NULL
    , prenume			VARCHAR(25) 
    
    , CONSTRAINT		ang_PK  PRIMARY KEY  (id_angajat)
	);
    
    
ALTER TABLE comanda
	ADD CONSTRAINT FK_Angajat
	FOREIGN KEY (id_angajat ) REFERENCES angajat(id_angajat) ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE transport
	( nr_masina	     	VARCHAR(7)  
    , firma_curierat	VARCHAR(25)   NOT NULL 
    , id_sofer			DECIMAL(4,0)  UNIQUE
    
    , CONSTRAINT		trans_PK  PRIMARY KEY  (nr_masina)
    , CONSTRAINT		trans_nr_check	CHECK (length(nr_masina)=7)
	);
    
ALTER TABLE comanda
	ADD CONSTRAINT FK_Transport
	FOREIGN KEY (nr_masina) REFERENCES transport(nr_masina) ON DELETE CASCADE ON UPDATE CASCADE;


CREATE TABLE magazin
	( id_magazin 		DECIMAL(4,0) 	
    , nume				VARCHAR(25) NOT NULL
    , localitate		VARCHAR(25) NOT NULL
    , strada			VARCHAR(25) NOT NULL
    , numar				DECIMAL(4,0) 
    
    , CONSTRAINT		magaz_PK  PRIMARY KEY  (id_magazin)
	);


ALTER TABLE comanda
	ADD CONSTRAINT FK_Magazin
	FOREIGN KEY (id_magazin) REFERENCES magazin(id_magazin)  ON DELETE CASCADE ON UPDATE CASCADE;


# date producator

insert into producator values(9638038, 'L`oreal Romania S.R.L', 'L`oreal', 'Bucuresti', 'Floreasca');
insert into producator values(36571040, 'Brand Essence S.R.L', 'Essence', 'Bucuresti', 'Opalului');
insert into producator values(211369, 'Cosmetic Plant Prodcom S.R.L', 'Cosmetic Plant', 'Cluj-Napoca', 'Traian Vuia');
insert into producator values(4240311, 'S.C. Sarantis Romania S.A', 'Elmiplant', 'Ploiesti', 'Rozelor');
insert into producator values(38659549, 'REVOLUTION MEDIA COMPANY SRL ', 'Revolution', 'Bucuresti', 'Academiei');


# date aprovizionare

insert into aprovizionare values(100000, 36571040, '2022-01-30');
insert into aprovizionare values(100001, 4240311, '2022-03-10');
insert into aprovizionare values(100002, 4240311, '2021-03-12');
insert into aprovizionare values(100003, 38659549, '2022-06-22');
insert into aprovizionare values(100004, 9638038, '2021-12-10');

# date cosmetice

insert into cosmetice values(10, 'Ruj', 'buze', 120, 35.5, '2023-01-10');
insert into cosmetice values(20, 'Fond de ten', 'fata', 60, 145.8, '2022-05-17');
insert into cosmetice values(30, 'Crema hidratanta', 'fata', 20, 90.0, '2023-10-21');
insert into cosmetice values(40, 'Mascara gene', 'ochi', 65, 55.5, '2023-12-30');
insert into cosmetice values(50, 'Lotiune de corp', 'corp', 18, 40, '2022-11-10');

# date facturi aprovizionare

insert into factura_a values(1, 100001, 20, 50, 145.8);
insert into factura_a values(2, 100003, 50, 10, 40);
insert into factura_a values(3, 100003, 30, 50, 90.0);

# date angajat

insert into angajat values(100,'Nemes', 'Tudor');
insert into angajat values(101,'Popa', 'Marius');
insert into angajat values(102,'Burgui', 'Roxana');
insert into angajat values(103,'Popescu', 'Elena');
insert into angajat values(104,'Marcu', 'Ioana');

# date magazin

insert into magazin values(1000, 'Nicole', 'Giurgiu', 'Norilor', 3);
insert into magazin values(1001, 'Eifel', 'Pitesti', 'Aviatorilor', 102);
insert into magazin values(1002, 'Stavros', 'Galati', 'Lalelelor', null);
insert into magazin values(1003, 'Adonis', 'Bucuresti', 'Principala', 22);
insert into magazin values(1004, 'Dimar', 'Buzau', 'Polis', null);

# date trnsport

insert into transport values('IF03GLS','GLS', 80);
insert into transport values('IF10FAN','Fan Curier', 81);
insert into transport values('IF11FAN','Fan Curier', 82);
insert into transport values('IF05GLS','GLS', 83);
insert into transport values('IF01CAR','Cargus', 84);

# date comanda
    
insert into comanda values(290500, '2021-10-21', '2021-10-23', 1001,  'IF10FAN', 100);
insert into comanda values(290501, '2021-12-30', '2022-01-03', 1003,  'IF05GLS', 103);
insert into comanda values(290502, '2021-06-20', '2021-07-01', 1003,  'IF03GLS', 101);
insert into comanda values(290503, '2020-11-12', '2020-11-15', 1000,  'IF01CAR', 102);
insert into comanda values(290504, '2022-01-05', null, 1004,  'IF01CAR', 100);

# date facturi comenzi

insert into factura_c values(1, 290501, 10, 20, 35.5);
insert into factura_c values(2, 290503, 40, 12, 55.5);
insert into factura_c values(3, 290503, 20, 30, 145.8);
insert into factura_c values(4, 290501, 20, 10, 145.8);


  

