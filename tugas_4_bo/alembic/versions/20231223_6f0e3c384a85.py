"""update

Revision ID: 6f0e3c384a85
Revises: 
Create Date: 2023-12-23 20:42:07.172889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "6f0e3c384a85"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "buku",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.Text(), nullable=True),
        sa.Column("description", sa.Text(), nullable=True),
        sa.Column("year", sa.Integer(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_buku")),
    )
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("name", sa.Text(), nullable=True),
        sa.Column("password", sa.Text(), nullable=True),
        sa.Column("email", sa.String(length=255), nullable=True),
        sa.Column("role", sa.Text(), nullable=True),
        sa.Column("token", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_user")),
        sa.UniqueConstraint("email", name=op.f("uq_user_email")),
    )
    op.create_index("user_email", "user", ["email"], unique=True, mysql_length=255)
    # ### end Alembic commands ###
    op.bulk_insert(
        sa.table(
            "user",
            sa.Column("name", sa.Text(), nullable=True),
            sa.Column("password", sa.Text(), nullable=True),
            sa.Column("email", sa.String(length=255), nullable=True),
            sa.Column("role", sa.Text(), nullable=True),
            sa.Column("token", sa.Text(), nullable=True),
        ),
        [
            {
                "name": "admin",
                "password": "admin",
                "email": "admin@admin.com",
                "role": "admin",
                "token": "",
            },
            {
                "name": "user",
                "password": "user",
                "email": "user@user.com",
                "role": "user",
                "token": "",
            },
        ],
    )

    op.bulk_insert(
        sa.table(
            "buku",
            sa.Column("title", sa.Text(), nullable=True),
            sa.Column("description", sa.Text(), nullable=True),
            sa.Column("year", sa.Integer(), nullable=True),
        ),
        [
            {
                "title": "To Kill a Mockingbird",
                "description": "Novel klasik karya Harper Lee tentang keadilan dan rasisme di Amerika Serikat.",
                "year": 1960,
            },
            {
                "title": "1984",
                "description": "Novel distopia karya George Orwell yang menggambarkan masyarakat yang diperintah oleh pemerintahan otoriter.",
                "year": 1949,
            },
            {
                "title": "The Great Gatsby",
                "description": "Novel karya F. Scott Fitzgerald yang menggambarkan kehidupan mewah di era Jazz Age Amerika.",
                "year": 1925,
            },
            {
                "title": "Pride and Prejudice",
                "description": "Novel klasik karya Jane Austen tentang cinta dan konvensi sosial di Inggris abad ke-19.",
                "year": 1813,
            },
            {
                "title": "Brave New World",
                "description": "Novel distopia karya Aldous Huxley yang menggambarkan masyarakat yang dikendalikan oleh teknologi dan konsumerisme.",
                "year": 1932,
            },
            {
                "title": "The Catcher in the Rye",
                "description": "Novel karya J.D. Salinger tentang pencarian identitas dan perjuangan remaja.",
                "year": 1951,
            },
            {
                "title": "Lord of the Flies",
                "description": "Novel karya William Golding yang menggambarkan perjuangan antara kebaikan dan kejahatan di antara sekelompok anak yang terdampar di pulau terpencil.",
                "year": 1954,
            },
            {
                "title": "The Hobbit",
                "description": "Novel fantasi karya J.R.R. Tolkien yang mengisahkan petualangan Bilbo Baggins.",
                "year": 1937,
            },
            {
                "title": "Frankenstein",
                "description": "Novel karya Mary Shelley yang menggambarkan penciptaan makhluk buatan manusia dan pertanyaan etika terkait kekuasaan manusia atas alam.",
                "year": 1818,
            },
            {
                "title": "Moby-Dick",
                "description": "Novel epik karya Herman Melville yang mengisahkan perburuan paus oleh Kapten Ahab.",
                "year": 1851,
            },
        ],
    )


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("user_email", table_name="user", mysql_length=255)
    op.drop_table("user")
    op.drop_table("buku")
    # ### end Alembic commands ###
