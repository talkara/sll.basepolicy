from plone.registry.interfaces import IRegistry
from sll.basepolicy.tests.base import IntegrationTestCase
from zope.component import getUtility

import mock


class TestCase(IntegrationTestCase):
    """TestCase for Plone upgrades."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_set_record_abita_development_rate(self):
        registry = getUtility(IRegistry)
        registry['abita.development.rate'] = 2.0
        self.assertEqual(registry['abita.development.rate'], 2.0)

        from sll.basepolicy.upgrades import set_record_abita_development_rate
        set_record_abita_development_rate(5.0)

        self.assertEqual(registry['abita.development.rate'], 5.0)

    @mock.patch('sll.basepolicy.upgrades.getToolByName')
    def test_reimport_profile(self, getToolByName):
        from sll.basepolicy.upgrades import reimport_profile
        reimport_profile(self.portal, 'PROFILE', 'NAME')
        getToolByName().runImportStepFromProfile.assert_called_with(
            'PROFILE', 'NAME', run_dependencies=False, purge_old=False)
