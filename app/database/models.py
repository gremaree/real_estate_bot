from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase
from sqlalchemy import Integer, String, Float

class Base(DeclarativeBase):
    pass

class RealEstate(Base):
    __tablename__ = "real_estate"

    id: Mapped[int] = mapped_column(primary_key=True)
    type: Mapped[str] = mapped_column(String)        # 'buy' или 'rent'
    title: Mapped[str] = mapped_column(String)
    address: Mapped[str] = mapped_column(String)
    area: Mapped[float] = mapped_column()
    price: Mapped[float] = mapped_column()
    contact_name: Mapped[str] = mapped_column(String)
    contact_phone: Mapped[str] = mapped_column(String)
    image_url: Mapped[str] = mapped_column(String)
    status: Mapped[str] = mapped_column(String)      # 'available', 'sold', 'rented'
