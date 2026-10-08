from pydantic import BaseModel, Field, ValidationError
from typing import List

# 1. Define a Pydantic Model (Data Blueprint)
class StudentProfile(BaseModel):
    # Field(...) indicates this field is REQUIRED
    roll_no: str = Field(..., description="Unique student ID, e.g. AI-101")
    name: str = Field(..., min_length=2, description="Student full name")
    
    # ge = Greater than or Equal to (0.0), le = Less than or Equal to (10.0)
    cgpa: float = Field(..., ge=0.0, le=10.0, description="Cumulative GPA")
    courses_enrolled: List[str] = Field(default_factory=list)
    has_library_dues: bool = Field(default=False)

# 2. Creating an instance (Notice: Pydantic automatically generates __init__!)
valid_student = StudentProfile(
    roll_no="AI-2026-001",
    name="Aarav Sharma",
    cgpa=8.75,
    courses_enrolled=["FastAPI", "Generative AI"]
)

print("✅ Successfully Validated Student Object:")
print(f"Name : {valid_student.name} | CGPA: {valid_student.cgpa}")

# 3. Export directly to clean JSON string
print("\nDirect JSON Serialization (.model_dump_json()):")
print(valid_student.model_dump_json(indent=2))

# 4. Watch Pydantic catch invalid data automatically!
print("\nTesting Pydantic Error Handling (Invalid CGPA = 14.5):")
try:
    StudentProfile(roll_no="AI-999", name="Test", cgpa=14.5)
except ValidationError as err:
    print("Caught expected validation error:")
    print(err.errors()[0]["msg"])