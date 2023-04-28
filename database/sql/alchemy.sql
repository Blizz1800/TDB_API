CREATE TABLE IF NOT EXISTS "alchemy" (
	"id" INTEGER NOT NULL,
	"seed" INTEGER NOT NULL,
	"plant" INTEGER NOT NULL,
	"event" INTEGER NOT NULL,
	"moon_phase" INTEGER NOT NULL,
	"min_time" TEXT NOT NULL,
	"max_time" TEXT NOT NULL,
	
	PRIMARY KEY("id" AUTOINCREMENT)
	FOREIGN KEY("seed") REFERENCES "items"("id") ON UPDATE CASCADE
	FOREIGN KEY("plant") REFERENCES "items"("id") ON UPDATE CASCADE
	FOREIGN KEY("event") REFERENCES "events"("id") ON UPDATE CASCADE
	FOREIGN KEY("moon_phase") REFERENCES "moons"("id") ON UPDATE CASCADE
);