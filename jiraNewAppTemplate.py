import jira.client
from jira import JIRA
from jira.exceptions import JIRAError
import unicodedata

# Be careful running this! It will create 28 initial Jira issues and assign them to those in the list
# It can't really be undone. Last line of code creates the issues


#Set these for each project
projectKey = 'PAC'
#assigneeName = "admin"  #username from Jira
issueType = "Story"

options = {'server': 'https://pointburst.atlassian.net'}
jira = JIRA(options, basic_auth=(' YOUR USERNAME ', 'YOUR PASSWORD'))


""" UNCOMMENT THIS SECTION TO ACTUALLY CREATE THE PROJECT TOO
# Extra section to create project too
user     = ' YOUR USERNAME '
projectName       ="  FULL NAME OF PROJECT  "
projassignee   =user
#jira.create_project(projectKey, projectName, projassignee, 'Scrum')
"""


issuesList = ["create google analytics ID",  # :'jeffreyrenken',
              "Add Google Analytics IDs", #: 'psrinivas',
                "color values (iOS)", #: 'psrinivas',
                "App authorization form (iOS and android)", #: 'mick.twomey',
                "Android - Twitter  app in the app's own backend cluster", #: 'sitakanta',
                "iOS - Twitter app in the app's own backend cluster", #: 'psrinivas',
                "Android - FB app in the app's own backend cluster", #: 'sitakanta',
                "iOS - FB app in the app's own backend cluster", #: 'psrinivas',
                "Android - New landing page", #: 'sitakanta',
                "iOS -New Landing page", #: 'psrinivas',
                "Android - Email sign up required for registartion", #: 'sitakanta',
                "iOS - Email sign up required for registration", #: 'psrinivas',
                "Android - FB compliance included", #: 'sitakanta',
                "iOS- FB compliance included", #: 'psrinivas',
                "Android- Integration with Kaltura", #: 'sitakanta',
                "iOS-Integration of Kaltura", #: 'psrinivas',
                "Upload publisher credentials", #: 'mick.twomey',
                "Upload iOS artwork", #: 'rogerrohatgi',
                "Create P12 files", #: 'psrinivas',
                "Android - Updates files on SVN for Apstrata and commit", #: 'yogi',
                "create google playstore images", #: 'sitakanta',
                "Create Apple App Store images", #: 'psrinivas',
                "Upload android artwork", #: 'rogerrohatgi',
                "Android - GP - Link Sender ID", #: 'sitakanta',
                "Android - Add GCM to APIs and Auth in GDC", #: 'sitakanta',
                "Android - Create project in Google Developer Console", #: 'sitakanta',
                "iOS - Create certificates", #: 'psrinivas',
                "iOS - Create Facebook suffix" #: 'mick.twomey',
                ]


assigneeList = ['jeffreyrenken',
                'psrinivas',
                'psrinivas',
                'mick.twomey',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'sitakanta',
                'psrinivas',
                'mick.twomey',
                'rogerrohatgi',
                'psrinivas',
                'yogi',
                'sitakanta',
                'psrinivas',
                'rogerrohatgi',
                'sitakanta',
                'sitakanta',
                'sitakanta',
                'psrinivas',
                'mick.twomey']


issue_dict = {}
i = 0
for things in issuesList:
    summary = issuesList[i]
    assignee = assigneeList[i]
    issue_dict = {
                 'project': {'key': projectKey},
                  'summary': summary,
                  'description': '',
                  'issuetype': {'name': issueType},
                  'assignee': {'name': assignee},
                   }
    i = i+1
    new_issue = jira.create_issue(fields=issue_dict)

