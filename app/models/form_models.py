from pydantic import BaseModel, EmailStr
from typing import Optional, List
from enum import Enum


class Gender(str, Enum):
    Male = "Male"
    Female = "Female"
    Other = "Other"


class PreferredContactMethod(str, Enum):
    Email = "Email"
    Phone = "Phone"


class PersonalInfo(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    gender: Optional[Gender]


class ContactInfo(BaseModel):
    email: Optional[EmailStr]
    phone: Optional[str]
    preferred_contact_method: Optional[PreferredContactMethod]
    call_reasons: Optional[List[str]]


class FormCompletionResponse(BaseModel):
    personal_info: PersonalInfo
    contact_info: ContactInfo


class FormCompletionRequest(BaseModel):
    text: str