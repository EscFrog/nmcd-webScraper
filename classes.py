class Job:
  def __init__(self, title, company, reward, link):
    self.title = title
    self.company = company
    self.reward = reward
    self.link = link

  def get_property_list(self):
    return [self.title, self.company, self.reward, self.link]