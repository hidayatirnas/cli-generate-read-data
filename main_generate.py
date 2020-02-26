from sqlalchemy import create_engine
from models import Base
from sqlalchemy.orm import sessionmaker
from generate import insert_user_device, generate_dummy_data
import argparse


if __name__ == "__main__":
    # create parser
    parser=argparse.ArgumentParser(
        prog='main_generate', 
        description='Generate data to sqlite format'
    )

    # add argument to the parser
    parser.add_argument('ndata', metavar='N', default=1000, type=int, help='Generate N data to db format')

    # parse the parser argument
    args=parser.parse_args()



    # create engine to connect to file
    engine=create_engine('sqlite:///efishery.db')
    Session=sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    session=Session()

    insert_user_device(session)
    generate_dummy_data(session, how_many=args.ndata)