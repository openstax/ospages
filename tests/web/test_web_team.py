"""Test the OpenStax team and advisor page."""

from pages.web.home import WebHome
from tests.markers import nondestructive, skip_test, test_case, web
from utils.utilities import Utility
from utils.web import Web


@test_case('C210455')
@nondestructive
@web
def test_the_openstax_team_is_split_into_three_groups(web_base_url, selenium):
    """The three group tabs are available.

    Note: FAB is currently missing and will be readded when
    the content is completed.
    """
    # GIVEN: a user viewing the team page
    home = WebHome(selenium, web_base_url).open()
    team = home.web_nav.openstax.view_team()

    # WHEN:

    # THEN: the "OpenStax Team", "Strategic Advisors", and
    #       "Faculty Advisory Board" are displayed
    assert(team.is_displayed())
    assert('team' in team.location)
    for tab in team.tabs:
        assert(tab.name in Web.TEAM_GROUPS), \
            '"{0}" not in the expected group list'.format(tab.name)


@test_case('C210456')
@nondestructive
@web
def test_selecting_a_team_member_opens_their_bio(web_base_url, selenium):
    """Test clicking on a staff member's card."""
    # GIVEN: a user viewing the team page
    home = WebHome(selenium, web_base_url).open()
    team = home.web_nav.openstax.view_team()

    # WHEN: they click on an OpenStax team member with a biography
    person = team.people[Utility.random(end=len(team.people) - 1)]
    while(not person.has_bio):
        person = team.people[Utility.random(end=len(team.people) - 1)]
    person.select()
    print(person.name)

    # THEN: a pop out pane displays the team member's bio
    assert(person.bio), 'Biography missing'

    # WHEN: they click on the team member again
    person.select()

    # THEN: the pop out pane is closed
    assert(not person.bio_visible)


@test_case('C210457')
@nondestructive
@web
def test_strategic_advisors_are_listed_with_their_bio(web_base_url, selenium):
    """Strategic advisors are listed with a short bio."""
    # GIVEN: a user viewing the team page
    home = WebHome(selenium, web_base_url).open()
    team = home.web_nav.openstax.view_team()

    # WHEN: they click on the "Strategic Advisors" tab
    team.tabs[Web.STRATEGIC_ADVISORS].select()

    # THEN: the strategic advisors are listed with their
    #       name
    for advisor in team.advisors:
        assert(advisor.name)


@skip_test(reason='FAB not currently available')
@test_case('C210458')
@nondestructive
@web
def test_advisory_board_members_are_listed_with_their_school(
        web_base_url, selenium):
    """FAB members are listed with their school affiliation."""
    # GIVEN: a user viewing the team page
    home = WebHome(selenium, web_base_url).open()
    team = home.web_nav.openstax.view_team()

    # WHEN: they click on the "Faculty Advisory Board" tab
    team.tabs[Web.ADVISORY_BOARD].select()

    # THEN: the advisory board members are listed with their
    #       photo and school
    for advisor in team.fab:
        assert(advisor.name)
        assert(advisor.has_image)
        assert(advisor.school)


@test_case('C210459')
@nondestructive
@web
def test_mobile_users_are_presented_bars(web_base_url, selenium):
    """On mobile, group tabs are replaced by accordion menus."""
    # GIVEN: a user viewing the team page
    # AND:  the screen width is 600 pixels
    home = WebHome(selenium, web_base_url)
    home.resize_window(width=600)
    home.open()
    home.web_nav.meta.toggle_menu()
    team = home.web_nav.openstax.view_team()

    for position, group in enumerate(team.bars):
        print(position, group.name)
        # WHEN: they click on the group bar
        group.toggle()

        # THEN: the team member tiles are displayed
        assert(group.is_open)
        if position == Web.OPENSTAX_TEAM:
            person = Utility.random(end=len(team.people) - 1)
            team.people[person].view()
            assert(team.people[person].is_visible)
        elif position == Web.STRATEGIC_ADVISORS:
            person = Utility.random(end=len(team.advisors) - 1)
            team.advisors[person].view()
            assert(team.advisors[person].is_visible)
        elif position == Web.ADVISORY_BOARD:
            person = Utility.random(end=len(team.fab) - 1)
            team.fab[person].view()
            assert(team.fab[person].is_visible)
        else:
            assert(False), \
                '"{0}" is not a recognized group'.format(group.name)

        # WHEN: they click on the group bar
        group.toggle()

        # THEN: the team member section is closed
        assert(not group.is_open)
