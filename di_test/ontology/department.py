from efficieno.ontology.columns_base import Column
from efficieno.ontology.relations_base import OneToOne, OneToMany, ManyToOne, ManyToMany
from efficieno.ontology.base import Ontology


class Department(Ontology):
    table_name = "scott.dept"

    dept_id = Column(name="deptno")
    dept_name = Column(name="dname")
    dept_location = Column(name="loc")

    @classmethod
    def validator(cls: "Ontology", field: Column, value):
        pass

    @classmethod
    def get_permissible_values(cls: "Ontology", field: Column):
        pass

    @classmethod
    def create_record(cls: "Ontology", new_value: dict):
        pass

    @classmethod
    def update_record(cls: "Ontology", update_record: dict):
        pass

    @classmethod
    def delete_record(cls: "Ontology", delete_record: dict):
        pass

