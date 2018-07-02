"""Test the Tutor teacher course roster functions."""

from tests.markers import expected_failure, nondestructive, test_case, tutor


@expected_failure
@test_case('')
@tutor
def test_add_a_new_section(tutor_base_url, selenium, teacher):
    """Add a new section in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click "add a section"
    # AND: Enter a section name, click enter

    # THEN: A new section should appear


@expected_failure
@test_case('')
@tutor
def test_add_a_new_instructor(tutor_base_url, selenium, teacher):
    """Add a new instruction in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click "add a new instructor"
    # AND: Add instructor name, click enter

    # THEN: A url link that instructor could use to join this course is shown


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_roster_switch_between_sections(tutor_base_url, selenium, teacher):
    """Switch view between sections in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click on another section

    # THEN: user is switched to the other section


@expected_failure
@test_case('')
@tutor
def test_rename_a_section(tutor_base_url, selenium, teacher):
    """Rename a section in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click "rename"
    # AND: Type in new name, click enter

    # THEN: Section is renamed


@expected_failure
@test_case('')
@tutor
def test_delete_a_section(tutor_base_url, selenium, teacher):
    """Delete a section in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the ""Course Roster"" page

    # WHEN: Click "delete section"
    # AND: Click "yes"

    # THEN: the section is deleted


@expected_failure
@nondestructive
@test_case('')
@tutor
def test_cancel_delete_a_section(tutor_base_url, selenium, teacher):
    """Cancel deleting a section in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click "delete a section"
    # AND: Click "cancel"

    # THEN: The section should not be deleted


@test_case('')
@tutor
def test_cancel_renaming_a_section(tutor_base_url, selenium, teacher):
    """Cancel renaming a section in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click "rename a section"
    # AND: Click "cancel"

    # THEN: The section name should not change


@test_case('')
@tutor
def test_edit_student_id(tutor_base_url, selenium, teacher):
    """Edit student id in course roster."""
    # GIVEN: Logged into Tutor as a teacher
    # AND: User is at the "Course Roster" page

    # WHEN: Click on the little pencil sign near student id

    # THEN: the student's id is edited