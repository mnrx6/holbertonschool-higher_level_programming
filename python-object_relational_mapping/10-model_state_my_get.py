#!/usr/bin/python3
"""Get a state ID by its name using SQLAlchemy."""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )

    session = Session(engine)
    state_name = sys.argv[4]

    state = session.query(State).filter_by(name=state_name).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
