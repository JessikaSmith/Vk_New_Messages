import vk

class vkontakte:

	def __init__(self, api_id, user_login, user_pass):
	
		self.session = vk.AuthSession(scope = 'messages', app_id = api_id, user_login = user_login, user_password = user_pass)
		self.api = vk.API(self.session)
		
	def get_last_messages(self):
		return self.api.messages.get(out = 0,count = 10)
		
	

