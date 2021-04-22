import graphene

from data import get_id, get_name, get_dob


class Person(graphene.Interface):
    id = graphene.ID()
    name = graphene.String()


class Student(graphene.ObjectType): #Student inherits from graphene.ObjType
    class Meta:
        interfaces = (Person,)
    dob = graphene.String()


class Query(graphene.ObjectType):
    hello = graphene.String(description='Hello World')
    studentById = graphene.Field(Student, id=graphene.String())
    studentByName = graphene.Field(Student, name=graphene.String())
    studentByDob = graphene.Field(Student, dob=graphene.String())

    def resolve_hello(self,info):
        return 'World'

    def resolve_studentById(self, info, id):
        return get_id(id)

    def resolve_studentByName(self, info, name):
        return get_name(name)

    def resolve_studentByDob(self, info, dob):
        return get_dob(dob)


schema = graphene.Schema(query=Query)
