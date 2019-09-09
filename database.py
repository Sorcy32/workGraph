import sqlite3
import os

name_db = 'database.db' #Изменить в будущем под конфигпарсер
cur_dir = os.getcwd()
path_db = os.path.join(cur_dir, name_db)


def create_database(path = path_db):
  '''
  Функция создает базу данных (путь и имя базы передать входным параметром)
  Создает в базе таблицы 'users' и 'dairy'. Заполняет заголовки к ним.
  '''
  conn = sqlite3.connect(path)
  cursor = conn.cursor()
  cursor.executescript("""
			BEGIN TRANSACTION;
			CREATE TABLE "users" (
				`user_id`    INTEGER PRIMARY KEY AUTOINCREMENT,
				`user_name`    TEXT,
				`user_area`    TEXT,
				`user_work_hours`    TEXT,
                `user_phone`    TEXT,
                `user_note`   TEXT,
                `user_current_tickets`    INT );
            CREATE TABLE "dairy" (
                `dairy_ID` INTEGER PRIMARY KEY AUTOINCREMENT,
                `dairy_date` TEXT,
                `dairy_user_id` TEXT,
                `dairy_workday_fact` BIT,
                `dairy_workday_official` BIT,
                `dairy_commentary` TEXT );
            CREATE TABLE "work_hours"(
                `work_hours_ID` INTEGER PRIMARY KEY AUTOINCREMENT,
                `work_hours_graph` TEXT );
            COMMIT; """)
  conn.commit()
print('Database created')


def add_user(user_name, user_area, user_work_hours, user_phone, user_note, user_current_tickets):
  '''
  Добавить пользователя в таблицу 'users'
		`user_name`               TEXT,          ФИО сотрудника
		`user_area`               TEXT,          Рабочий район сотрудника
		`user_work_hours`         TEXT,          График работы
        `user_phone`              TEXT,          Телефон сотрудника
        `user_note`               TEXT,          Комментарий
        `user_current_tickets`    INT Текущее количество нарядов ( default = 0)
  '''
  '''INSERT INTO `user`  (user_name, id_lang, changed)
			VALUES('Егор',1, DATETIME('now'));
			INSERT INTO `user`  (name, id_lang, changed)
			VALUES('Иван',2, DATETIME('now'));'''
