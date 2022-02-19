from __future__ import annotations
from collections import defaultdict
from datetime import date
from typing import Dict, List
import pytest
from src.barkylib import bootstrap
from src.barkylib.domain import commands
from src.barkylib.services import handlers, unit_of_work
from src.barkylib.adapters import repository

class FakeRepository(repository.AbstractRepository):
    def __init__(self, products):
        super().__init__()
        self._products = set(products)

    def _add(self, product):
        self._products.add(product)

    def _get(self, sku):
        return next((p for p in self._products if p.sku == sku), None)

    def _get_by_batchref(self, batchref):
        return next(
            (p for p in self._products for b in p.batches if b.reference == batchref),
            None,
        )