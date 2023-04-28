CREATE TABLE IF NOT EXISTS "recipes" ( 
	"id" INTEGER NOT NULL, 
	"table" INTEGER NOT NULL, 
	"name" INTEGER NOT NULL, 
	"quantity" INTEGER NOT NULL, 
	"ingredients" TEXT NOT NULL, 

	PRIMARY KEY("id" AUTOINCREMENT), 
	FOREIGN KEY("table") REFERENCES "tables"("id") ON UPDATE CASCADE, 
	FOREIGN KEY("name") REFERENCES "items"("id") ON UPDATE CASCADE
);