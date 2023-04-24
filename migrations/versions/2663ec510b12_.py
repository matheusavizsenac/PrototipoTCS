"""empty message

Revision ID: 2663ec510b12
Revises: 
Create Date: 2023-04-24 11:06:00.240551

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2663ec510b12'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('historias',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('descricao', sa.String(length=256), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('historias')
    # ### end Alembic commands ###