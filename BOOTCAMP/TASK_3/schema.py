import graphene
import graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType,SQLAlchemyConnectionField
from .model import db_session,Department as DepartmentModel, Employee as EmployeeModel

class Department(SQLAlchemyObjectType):
    class Meta:
        model = DepartmentModel
        interfaces = (relay.Node,)
class DepartmentConnection(relay.Connection):
    class Meta:
        note = Department
class Employee(SQLAlchemyObjectType):
    class Meta:
        model = EmployeeModel
        interfaces = (relay.Node)
class EmployeeConnection(relay.Connection):
    class Meta:
        note = Employee
class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_employees = SQLAlchemyConnectionField(EmployeeConnection)
    all_departments = SQLAlchemyConnectionField(DepartmentConnection)
schema = graphene.Schema(query=Query)
