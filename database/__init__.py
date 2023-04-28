import sqlite3
import json
from configparser import ConfigParser


class Database:

    def __init__(self, verbose=False):
        self.__db__ = sqlite3.connect('./database_v2.db')
        self.__cursor__ = self.__db__.cursor()
        self.__current_json__ = None
        self.__current_sql__ = None
        self.__config__ = ConfigParser()
        self.__config__.read('./database/config.ini')
        self.VERB = verbose

    def __load_json__(self, json_db):
        if self.__current_json__ is not None:
            self.__current_json__.close()
        self.__current_json__ = open(f"./database/json_data/{json_db}.json", 'r')
        return self.__current_json__

    def __load_sql__(self, sql_file):
        if self.__current_sql__ is not None:
            self.__current_sql__.close()
        self.__current_sql__ = open(f"./database/sql/{sql_file}.sql", 'r')
        return self.__current_sql__

    @staticmethod
    def __generate_insert__(data):
        resp = "(\"" + "\", \"".join(data) + "\")"
        return resp

    def __init_tables__(self):
        tables = ['items', 'tables', 'recipes', 'events', 'moon', "buffs", 'alchemy']
        for t in tables:
            self.__cursor__.execute(self.__load_sql__(t).read())

    def __destroy_all__(self, table):
        self.__cursor__.execute(f"DELETE FROM {table}")

    def __init_c_tables__(self):
        f = self.__load_json__('tables')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO tables (id, name, a_name) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        items.append(self.__generate_insert__([c_item['id'], c_item['name'], c_item['alternate_name']]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __init_events__(self):
        f = self.__load_json__('events')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO events (id, name, hardmode) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        items.append(self.__generate_insert__([c_item['id'], c_item['name'], c_item['hardmode']]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __init_moon__(self):
        f = self.__load_json__('moon')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO moon (id, name) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        items.append(self.__generate_insert__([c_item['id'], c_item['name']]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __init_buffs__(self):
        f = self.__load_json__('buffs')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO buffs (id, name, effect, duration) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        items.append(self.__generate_insert__([c_item['id'], c_item['name'], c_item['effect'], c_item['duration']]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __init_alchemy__(self):
        f = self.__load_json__('alchemy')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO alchemy (id, seed, plant, event, moon_phase, min_time, max_time) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        items.append(self.__generate_insert__([c_item['id'], c_item['seed'], c_item['plant'], c_item['event'], c_item['moon_phase'], c_item['min_time'], c_item['max_time']]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __init_items__(self):
        f = self.__load_json__('items')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO items (id, name, recipes) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        recipes = []
                        for recipe_i in range(1, 7):
                            r = c_item['recipe' + str(recipe_i)]
                            if r == '':
                                break
                            recipes.append(r)
                        items.append(self.__generate_insert__([c_item['id'], c_item['name'], ",".join(recipes)]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __init_recipes__(self):
        f = self.__load_json__('recipes')
        data: list = json.loads(f.read())

        def repeat(__i=0, __steps=50):
            for i in range(__i, len(data), __steps):
                try:
                    items = []
                    query = "INSERT INTO recipes (id, \"table\", name, quantity, ingredients) VALUES "
                    for o in range(i, i + __steps):
                        c_item: dict = data[o]
                        ingredients = []
                        for ingredient_i in range(1, 7):
                            ing = c_item['ingredient' + str(ingredient_i)]
                            a = c_item['amount' + str(ingredient_i)]
                            if ing == '':
                                break
                            ingredients.append(",".join([ing, a]))
                        items.append(self.__generate_insert__(
                            [
                                c_item['id'], c_item['table'], c_item['name'],
                                c_item['quantity'], ";".join(ingredients)
                            ]))
                    query += ", ".join(items)
                    self.__cursor__.execute(query)
                    self.__db__.commit()
                except IndexError:
                    repeat(i, int(__steps / 2))
                    break

        repeat()
        f.close()

    def __update_buffs__(self):
        if self.VERB:
            print(" * Creating buffs in database")
        self.__destroy_all__('buffs')
        self.__init_buffs__()
        if self.VERB:
            print(" * Buffs created success!\n")

    def __update_items__(self):
        if self.VERB:
            print(" * Creating items in database")
        self.__destroy_all__('items')
        self.__init_items__()
        if self.VERB:
            print(" * Items created success!\n")

    def __update_recipes__(self):
        if self.VERB:
            print(" * Creating recipes in database")

        self.__destroy_all__('recipes')
        self.__init_recipes__()

        if self.VERB:
            print(" * Recipes created success!\n")

    def __update_c_tables__(self):
        if self.VERB:
            print(" * Creating crafting tables in database")

        self.__destroy_all__('tables')
        self.__init_c_tables__()

        if self.VERB:
            print(" * Crafting tables created success!\n")

    def __update_moon__(self):
        if self.VERB:
            print(" * Creating moons in database")

        self.__destroy_all__('moon')
        self.__init_moon__()

        if self.VERB:
            print(" * Moons created success!\n")

    def __update_events__(self):
        if self.VERB:
            print(" * Creating events in database")

        self.__destroy_all__('events')
        self.__init_events__()

        if self.VERB:
            print(" * Events created success!\n")

    def __update_alchemy__(self):
        if self.VERB:
            print(" * Creating alchemy in database")

        self.__destroy_all__('alchemy')
        self.__init_alchemy__()

        if self.VERB:
            print(" * Alchemy created success!\n")

    def __update_conf__(self, conf, value, section='Database'):
        self.__config__.set(section, conf, str(value))

    def __read_config__(self, conf, section='Database'):
        resp = self.__config__[section][conf]
        if resp.isdigit():
            return int(resp)
        else:
            return resp

    def set_verbosity(self, verb: bool):
        """
        Set verbosity of functions
        :param verb: Set verbosity value from it
        """
        self.VERB = verb

    def init(self):
        """
        Initialize the database!
        """
        self.__init_tables__()

        if self.__read_config__('items') == 0:
            self.__update_items__()
            self.__update_conf__('items', 1)

        if self.__read_config__('tables') == 0:
            self.__update_c_tables__()
            self.__update_conf__('tables', 1)

        if self.__read_config__('recipes') == 0:
            self.__update_recipes__()
            self.__update_conf__('recipes', 1)

        if self.__read_config__('moon') == 0:
            self.__update_moon__()
            self.__update_conf__('moon', 1)

        if self.__read_config__('events') == 0:
            self.__update_events__()
            self.__update_conf__('events', 1)

        if self.__read_config__('buffs') == 0:
            self.__update_buffs__()
            self.__update_conf__('buffs', 1)

        if self.__read_config__('alchemy') == 0:
            self.__update_alchemy__()
            self.__update_conf__('alchemy', 1)

        self.__config__.write(open('./database/config.ini', "+w"))


