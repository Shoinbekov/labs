package com.example;

import com.example.domain.Employee;
import java.text.NumberFormat;

public class EmployeeTest {
    public static void main(String[] args) {
        // Создаем первого сотрудника
        Employee emp1 = new Employee();
        emp1.setEmpId(101);
        emp1.setName("Jane Smith");
        emp1.setSsn("012-34-5678");
        emp1.setSalary(120_345.27);

        // Выводим данные первого сотрудника
        System.out.println("Employee 1:");
        System.out.println("ID: " + emp1.getEmpId());
        System.out.println("Name: " + emp1.getName());
        System.out.println("SSN: " + emp1.getSsn());
        System.out.println("Salary: " + 
            NumberFormat.getCurrencyInstance().format(emp1.getSalary()));

        System.out.println();

        // Создаем второго сотрудника
        Employee emp2 = new Employee();
        emp2.setEmpId(102);
        emp2.setName("John Doe");
        emp2.setSsn("123-45-6789");
        emp2.setSalary(98_765.43);

        // Выводим данные второго сотрудника
        System.out.println("Employee 2:");
        System.out.println("ID: " + emp2.getEmpId());
        System.out.println("Name: " + emp2.getName());
        System.out.println("SSN: " + emp2.getSsn());
        System.out.println("Salary: " + 
            NumberFormat.getCurrencyInstance().format(emp2.getSalary()));
    }
}

