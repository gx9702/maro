# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.


from maro.backends.backend import AttributeType
from maro.backends.frame import NodeAttribute

from .base import DataModelBase


class SkuDataModel(DataModelBase):
    # Product id of this consumer belongs to.
    product_id = NodeAttribute(AttributeType.UInt)

    # Parent unit id.
    product_unit_id = NodeAttribute(AttributeType.UInt)

    def __int__(self):
        super(SkuDataModel, self).__int__()

        self._product_id = 0
        self._product_unit_id = 0

    def reset(self):
        super(SkuDataModel, self).reset()

        self.product_id = self._product_id
        self.product_unit_id = self._product_unit_id

    def set_product_id(self, product_id: int, product_unit_id: int):
        self._product_id = product_id
        self._product_unit_id = product_unit_id
