import uuid

from sqlalchemy import Float, ForeignKey, Integer
from sqlalchemy.orm import Mapped, mapped_column

from app.database import Base


class RetrievalLogChunk(Base):
    __tablename__ = "retrieval_log_chunks"

    retrieval_log_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("retrieval_logs.id", ondelete="CASCADE"), primary_key=True
    )
    chunk_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("document_chunks.id", ondelete="CASCADE"),
        primary_key=True,
        index=True,
    )
    rank: Mapped[int] = mapped_column(Integer)
    score: Mapped[float] = mapped_column(Float)