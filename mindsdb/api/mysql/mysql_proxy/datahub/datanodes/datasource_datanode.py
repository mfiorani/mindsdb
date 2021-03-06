import json

import pandas

from mindsdb.api.mysql.mysql_proxy.datahub.datanodes.datanode import DataNode
# from mindsdb.interfaces.native.mindsdb import MindsdbNative
from mindsdb.interfaces.datastore.datastore import DataStore
from mindsdb.integrations.clickhouse.clickhouse import Clickhouse
from mindsdb.integrations.mariadb.mariadb import Mariadb


class DataSourceDataNode(DataNode):
    type = 'mindsdb-datasource'

    def __init__(self, config):
        self.config = config
        self.datastore = DataStore(config)
        # self.mindsdb_native = MindsdbNative(config)

    def getTables(self):
        dss = self.datastore.get_datasources()
        return [x['name'] for x in dss]

    def hasTable(self, table):
        return table in self.getTables()

    def getTableColumns(self, table):
        ds = self.datastore.get_datasource(table)
        return [x['name'] for x in ds['columns']]

    def select(self, table, columns=None, where=None, where_data=None, order_by=None, group_by=None, came_from=None):
        data = self.datastore.get_data(table, where=None, limit=None, offset=None)
        return data['data']
