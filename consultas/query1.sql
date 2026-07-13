SELECT
    e.employee_id,
    e.first_name || ' ' || e.last_name AS employee_name,
    j.job_title,
    d.department_name,
    e.salary,
    e.hire_date

FROM HR.EMPLOYEES e

LEFT JOIN HR.DEPARTMENTS d
ON e.department_id = d.department_id

LEFT JOIN HR.JOBS j
ON e.job_id = j.job_id

WHERE e.department_id IS NOT NULL;