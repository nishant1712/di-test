from efficieno.ontology.columns_base import Column
from efficieno.ontology.relations_base import OneToOne, OneToMany, ManyToOne, ManyToMany
from efficieno.ontology.base import Ontology
from .department import Department
from efficieno.ontology.query_builder import Fn, Select
from efficieno.ontology.relations_base import ManyToOne
from efficieno.components.table import Table


class Employee(Ontology):
    table_name = "scott.emp"

    emp_id = Column(name="empno")
    emp_name = Column(name="ename")
    job = Column(name="job")
    manager = Column(name="mgr")
    hire_date = Column(name="hiredate")
    salary = Column(name="sal")
    comm = Column(name="comm")
    dept_no = ManyToOne(name="deptno", relation_table_cols=Department.dept_id)

    table_view = (Table(table_name="Demo Table", sub_heading="Demo")
                  .add_column(dept_no, enable_column_filter=True)
                  .add_column(Fn.count(emp_id).alias("Count of emp "), enable_column_filter=True)
                  .filter(emp_id > 1)
                  # .filter(Employee.dept_no == 1)
                  .group_by(dept_no))

    table_view_again = (Table(table_name="Demo Table", sub_heading="Demo")
                        .add_column(dept_no, enable_column_filter=True)
                        .add_column(Fn.count(emp_id).alias("Count of emp "), enable_column_filter=True)
                        .filter(emp_id > 1)
                        # .filter(Employee.dept_no == 1)
                        .group_by(dept_no))

    @classmethod
    def validator(cls: "Ontology", field: Column, value):
        print(f"Calling validator for {field} with value {value}")

        if Employee.emp_id.name == field:
            print("Validating Employee ID ")
            if isinstance(value, int):
                return True
            else:
                raise ValueError

        if Employee.salary.name == field:
            print("Validating Employee Salary ")
            if isinstance(value, int):
                return True
            else:
                raise ValueError

        if Employee.dept_no.name == field:
            print("Validating Employee Department no ")
            val_statement = Select(Fn.count(Department.dept_id).alias("count")).filter(Department.dept_id == value)
            result = val_statement.execute()
            if result[0]["count"] >= 1:
                return True
            else:
                raise ValueError

    @classmethod
    def get_permissible_values(cls: "Ontology", field: Column):
        # if Employee.emp_id == field:
        #     print(f"Calling Permissible values for {field}")
        # print(f"Calling Permissible for {field} ")

        if Employee.dept_no.name == field:
            print("Validating Employee Department no ")
            val_statement = Select(Fn.distinct(Department.dept_id).alias("dept_id"))
            result = val_statement.execute()
            print(result)
            return result
            # if result[0]["count"] >= 1:
            #     return True
            # else:
            #     raise ValueError
        return True

    @classmethod
    def create_record(cls: "Ontology", new_value: dict):
        pass

    @classmethod
    def update_record(cls: "Ontology", update_record: dict):
        pass

    @classmethod
    def delete_record(cls: "Ontology", delete_record: dict):
        pass

