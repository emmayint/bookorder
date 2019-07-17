"""create tables

Revision ID: af05023c2b7d
Revises: 
Create Date: 2019-07-08 14:23:14.444023

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, Column, Float, Integer, BigInteger, String, MetaData, DateTime, ForeignKey, Enum


# revision identifiers, used by Alembic.
revision = 'af05023c2b7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'book',
        sa.Column('id', Integer, primary_key=True),
        sa.Column('title', String(255), nullable=False)
    )
    op.create_table(
        'order',
        sa.Column('id', Integer, primary_key=True),
        sa.Column('quantity', Integer)
    )


def downgrade():
    op.drop_table('book')
    op.drop_table('order')
