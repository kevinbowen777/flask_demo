"""empty message

Revision ID: 6889b93062eb
Revises: fb4b3feee411
Create Date: 2022-01-25 20:35:51.317065

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6889b93062eb'
down_revision = 'fb4b3feee411'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'body_html')
    # ### end Alembic commands ###
