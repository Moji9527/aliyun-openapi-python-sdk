# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest

class ModifyReadOnlyAccountPasswordRequest(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Drds', '2017-10-16', 'ModifyReadOnlyAccountPassword','drds')

	def get_NewPasswd(self):
		return self.get_query_params().get('NewPasswd')

	def set_NewPasswd(self,NewPasswd):
		self.add_query_param('NewPasswd',NewPasswd)

	def get_DbName(self):
		return self.get_query_params().get('DbName')

	def set_DbName(self,DbName):
		self.add_query_param('DbName',DbName)

	def get_AccountName(self):
		return self.get_query_params().get('AccountName')

	def set_AccountName(self,AccountName):
		self.add_query_param('AccountName',AccountName)

	def get_OriginPassword(self):
		return self.get_query_params().get('OriginPassword')

	def set_OriginPassword(self,OriginPassword):
		self.add_query_param('OriginPassword',OriginPassword)

	def get_DrdsInstanceId(self):
		return self.get_query_params().get('DrdsInstanceId')

	def set_DrdsInstanceId(self,DrdsInstanceId):
		self.add_query_param('DrdsInstanceId',DrdsInstanceId)