from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey

MeteData = MetaData()

roles = Table(
    "roles",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("permission", JSON),
)

users = Table(
    "users",
    Column("id", Integer, prymari_key=True),
    Column("email", String, nullable=False),
    Column("username", String, nullable=False),
    Column("password", String, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime, utcnow),
    Column("role_id", Integer, ForeignKey("roles.id")),
)