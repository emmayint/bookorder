"""add foreign key

Revision ID: 6d44d9559a99
Revises: af05023c2b7d
Create Date: 2019-07-08 14:25:55.737956

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import Table, Column, Float, Integer, BigInteger, String, MetaData, DateTime, ForeignKey, Enum


# revision identifiers, used by Alembic.
revision = '6d44d9559a99'
down_revision = 'af05023c2b7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('order', sa.Column('book_id', Integer, ForeignKey("book.id", onupdate="CASCADE", ondelete="CASCADE")))


def downgrade():
    op.drop_column('order', 'book_id')
