from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Transaction
from read import read_100, read_avg, read_by_filter, read_count, read_max, read_min, read_specific_row, read_sum, print_table, split_string_by_tab
import argparse

if __name__ == "__main__":
    # create parser
    parser=argparse.ArgumentParser(
        prog='main_read', 
        description='Read data from sqlite file that has been generated'
    )
    
    # add argument to the parser
    parser.add_argument('--show', nargs=1, metavar='X', choices=['asc', 'desc'], help='Show 100 data (ascending or descending to timestamp)')
    parser.add_argument('--filter', nargs=2, metavar='X', help="Filter by column by column name and it's value")
    parser.add_argument('--nrow', nargs=1, type=int, help="Show data in row n")
    parser.add_argument('--max', nargs=1, choices=['all', 'device_id', 'username', 'lokasi'], help="Show max amount (default: from all data, not grouped)")
    parser.add_argument('--min', nargs=1, choices=['all', 'device_id', 'username', 'lokasi'], help="Show min amount (default: from all data, not grouped)")
    parser.add_argument('--avg', nargs=1, choices=['all', 'device_id', 'username', 'lokasi'], help="Show average amount (default: from all data, not grouped)")
    parser.add_argument('--sum', nargs=1, choices=['all', 'device_id', 'username', 'lokasi'], help="Show sum amount (default: from all data, not grouped)")
    parser.add_argument('--count', nargs=1, choices=['all', 'device_id', 'username', 'lokasi'], help="Show count amount (default: from all data, not grouped)")

    # parse the parser argument
    args=parser.parse_args()



    # create engine to connect to file
    engine=create_engine('sqlite:///efishery.db')
    Session=sessionmaker(bind=engine)
    session=Session()

    # do the operation
    cols=['id', 'device_id', 'username', 'lokasi', 'amount', 'timestamp']
    if args.show:
        if args.show[0]=='asc':
            result=read_100(session)
        elif args.show[0]=='desc':
            result=read_100(session, False)
        data=[rresult.__repr__().split('\t') for rresult in result]
        print(print_table(data, cols))
    elif args.filter:
        result=read_by_filter(session, args.filter[0], args.filter[1])
        data=[rresult.__repr__().split('\t') for rresult in result]
        print(print_table(data, cols))
    elif args.nrow:
        result=read_specific_row(session, args.nrow[0])
        data=[result.__repr__().split('\t')]
        print(print_table(data, cols))
    elif args.max:
        result=read_max(session, args.max[0])
        if args.max[0]=='all':
            cols=['max']
            print(print_table(result, cols))
        else:
            cols=[args.max[0], 'max']
            result=[list(rresult) for rresult in result]
            print(print_table(result, cols))
    elif args.min:
        result=read_min(session, args.min[0])
        if args.min[0]=='all':
            cols=['min']
            print(print_table(result, cols))
        else:
            cols=[args.min[0], 'min']
            result=[list(rresult) for rresult in result]
            print(print_table(result, cols))
    elif args.avg:
        result=read_avg(session, args.avg[0])
        if args.avg[0]=='all':
            cols=['avg']
            print(print_table(result, cols))
        else:
            cols=[args.avg[0], 'avg']
            result=[list(rresult) for rresult in result]
            print(print_table(result, cols))
    elif args.sum:
        result=read_sum(session, args.sum[0])
        if args.sum[0]=='all':
            cols=['sum']
            print(print_table(result, cols))
        else:
            cols=[args.sum[0], 'sum']
            result=[list(rresult) for rresult in result]
            print(print_table(result, cols))
    elif args.count:
        result=read_count(session, args.count[0])
        if args.count[0]=='all':
            cols=['count']
            print(print_table(result, cols))
        else:
            cols=[args.count[0], 'count']
            result=[list(rresult) for rresult in result]
            print(print_table(result, cols))