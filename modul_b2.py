# We import the entire module and call it m_a
import modul_a as m_a

print(m_a.test)
courses = ["PE", "History", "Math"]
index = m_a.find_index(courses, "PE")
print(index)  # Prints 0
