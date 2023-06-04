"""empty message

Revision ID: dbd9807c5d80
Revises: 9a2fd4478684
Create Date: 2023-05-27 18:10:36.032154

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'dbd9807c5d80'
down_revision = '9a2fd4478684'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=mysql.VARCHAR(length=80),
               type_=sa.String(length=500),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('usuarios', schema=None) as batch_op:
        batch_op.alter_column('password',
               existing_type=sa.String(length=500),
               type_=mysql.VARCHAR(length=80),
               existing_nullable=True)

    # ### end Alembic commands ###