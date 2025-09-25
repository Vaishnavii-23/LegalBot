# legal_drafter_task.py

from crewai import Task

from agents.legal_drafter_agent import legal_drafter_agent
from tasks.case_intake_task import case_intake_task
from tasks.ipc_section_task import ipc_section_task
from tasks.legal_precedent_task import legal_precedent_task

legal_drafter_task = Task(
    agent=legal_drafter_agent,
    description=(
        "Based on the legal case summary, IPC sections, and precedents retrieved form the previous tasks, draft a formal legal document (e.g., FIR or legal notice) "
        "that the user can submit to the authorities or use for legal action.\n\n"
        "Draft a clear and properly formatted legal notice or complaint that is appropriate to this situation. "
        "The document should include a subject line, date, involved parties, factual background, applicable legal sections, and a formal request for action."
    ),
    expected_output=(
        "A formal legal document such as:\n"
        "- Title (e.g., LEGAL COMPLAINT)\n"
        "- Parties involved\n"
        "- Factual summary\n"
        "- Applicable legal sections\n"
        "- Demand or request\n"
        "- Date and sender details"
    ),
    context=[case_intake_task, ipc_section_task, legal_precedent_task]
)
