from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

from config import database_url
from database import read_data, get_data
from models import create_tables, drop_tables


def main():
    engine = create_engine(url=database_url())
    drop_tables(engine)
    create_tables(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    read_data(session=session, file_name="tests_data.json")
    get_data(session, "1")
    print('*' * 100)
    get_data(session, "Microsoft Press")

    session.close()


if __name__ == "__main__":
    main()
