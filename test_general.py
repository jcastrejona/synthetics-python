import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time 
import keyboard
# install keyboard and selenium using pip before running ******************************************************

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'


class TestGeneral:
  def setup_method(self):
    self.vars = {}

    #self.driver = webdriver.Chrome()
    self.driver = webdriver.Chrome(chrome_options=chrome_options)  
    self.driver.get("http://13.72.75.125/")
    self.driver.maximize_window()
    self.driver.implicitly_wait(2)
    self.driver.find_element_by_name("User").click()
    self.driver.find_element_by_name("User").send_keys("jose.castrejon")
    self.driver.find_element_by_name("Password").click()
    self.driver.find_element_by_name("Password").send_keys("admin")
    self.driver.find_element_by_xpath('//*[@id="ctc"]/div[2]/form/div[4]/button').click()

  def teardown_method(self):
    self.driver.quit()

  # method for waiting for a new tab
  def wait_for_window(self, timeout = 2):
    time.sleep(round(timeout / 1000))
    wh_now = self.driver.window_handles
    wh_then = self.vars["window_handles"]
    if len(wh_now) > len(wh_then):
      return set(wh_now).difference(set(wh_then)).pop()
  

  # Projects -------------------------------------------------------------------------------
  def test_CrearYBorrarProjecto(self):
    driver = self.driver
    driver.find_element_by_link_text("Projects").click()  
    driver.find_element_by_class_name("fa-plus-circle").click()
    driver.find_element_by_id("New").click()
    driver.find_element_by_id("New").send_keys("TESTSYN")
    driver.find_element_by_id("Register").click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="divSearch"]/input').click()
    driver.find_element_by_xpath('//*[@id="divSearch"]/input').send_keys("TESTSYN")
    action = ActionChains(driver)
    firstLevelMenu = driver.find_element_by_xpath('//*[@id="example"]/tbody/tr/td[2]')
    action.move_to_element(firstLevelMenu).perform()    
    driver.find_element_by_class_name('fa-trash').click()
    assert driver.switch_to.alert.text == "¿ESTA SEGURO QUE DESEA ELIMINAR ESTOS DATOS DE FORMA PERMANENTE? "
    driver.switch_to.alert.accept()
    assert driver.title == "Coelens"

# Community ---------------------------------------------------------------------
  def test_CrearYBorrarNuevoPillar(self):
    self.driver.find_element(By.LINK_TEXT, "Community").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active li:nth-child(1) span").click()
    self.driver.find_element(By.LINK_TEXT, "Pillar").click()
    self.driver.find_element(By.NAME, "Name").send_keys("test")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.LINK_TEXT, "Community").click()
    self.driver.find_element(By.LINK_TEXT, "All Community").click()
    self.driver.find_element(By.LINK_TEXT, "Category").click()
    self.driver.find_element(By.ID, "Pillars").click()
    dropdown = self.driver.find_element(By.ID, "Pillars")
    dropdown.find_element(By.XPATH, "//option[. = 'test']").click()
    self.driver.find_element(By.ID, "Pillars").click()
    self.driver.find_element(By.NAME, "Name").click()
    self.driver.find_element(By.NAME, "Name").send_keys("test")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element(By.LINK_TEXT, "Community").click()
    self.driver.find_element(By.LINK_TEXT, "All Community").click()
    self.driver.find_element(By.CSS_SELECTOR, ".contenido:nth-child(3) .fa").click()
    self.driver.find_element(By.ID, "Categories").click()
    dropdown = self.driver.find_element(By.ID, "Categories")
    dropdown.find_element(By.XPATH, "//option[. = 'test']").click()
    self.driver.find_element(By.ID, "Categories").click()
    self.driver.find_element(By.NAME, "Name").click()
    self.driver.find_element(By.NAME, "Name").send_keys("test")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    self.driver.find_element_by_xpath('//*[@id="divSearch"]/input').click()
    self.driver.find_element_by_xpath('//*[@id="divSearch"]/input').send_keys("test")
    action = ActionChains(self.driver)
    firstLevelMenu = self.driver.find_element_by_xpath('//*[@id="example"]/tbody/tr/td[2]')
    action.move_to_element(firstLevelMenu).perform()    
    self.driver.find_element_by_class_name('fa-trash').click()
    assert self.driver.switch_to.alert.text == "¿ESTA SEGURO QUE DESEA ELIMINAR ESTOS DATOS DE FORMA PERMANENTE? "
    self.driver.switch_to.alert.accept()
    assert self.driver.title == "Coelens"
  
  def test_CrearBadge(self):
    self.driver.find_element(By.LINK_TEXT, "Community").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active li:nth-child(2) span").click()
    self.driver.find_element(By.ID, "Tools").click()
    dropdown = self.driver.find_element(By.ID, "Tools")
    dropdown.find_element(By.XPATH, "//option[. = 'test']").click()
    self.driver.find_element(By.ID, "Tools").click()
    self.driver.find_element(By.NAME, "Name").click()
    self.driver.find_element(By.NAME, "Name").send_keys("test")
    self.driver.find_element(By.ID, "Level").click()
    dropdown = self.driver.find_element(By.ID, "Level")
    dropdown.find_element(By.XPATH, "//option[. = '1']").click()
    self.driver.find_element(By.ID, "Level").click()
    self.driver.find_element(By.NAME, "Description").click()
    self.driver.find_element(By.NAME, "Description").send_keys("test")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-success").click()
    assert self.driver.find_element_by_class_name("alert-success").is_displayed

  def test_LinkAllBadges(self):
    self.driver.find_element(By.LINK_TEXT, "Community").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active li:nth-child(3) > a").click()
    assert self.driver.find_element_by_xpath("/html/body/div[2]/main/div/div/div/div/div/div[1]/h4").is_displayed

  # Colaborators ------------------------------------------------------------------------------------------
  def test_CrearColaborador(self):
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-dropdown:nth-child(4) > a > span").click()
    self.driver.find_element(By.LINK_TEXT, "All Collaborators").click()
    self.driver.find_element(By.LINK_TEXT, "New").click()
    self.driver.find_element(By.ID, "is_colaborator").click()
    self.driver.find_element(By.ID, "is_colaborator").send_keys("test1")
    self.driver.find_element(By.NAME, "Name").click()
    self.driver.find_element(By.NAME, "Name").send_keys("test1")
    self.driver.find_element(By.NAME, "LastName").click()
    self.driver.find_element(By.NAME, "LastName").send_keys("test1")
    self.driver.find_element(By.ID, "Gender").click()
    dropdown = self.driver.find_element(By.ID, "Gender")
    dropdown.find_element(By.XPATH, "//option[. = 'Male']").click()
    self.driver.find_element(By.ID, "Gender").click()
    self.driver.find_element(By.NAME, "Role").click()
    self.driver.find_element(By.NAME, "Role").send_keys("test1")
    self.driver.find_element(By.ID, "Market").click()
    dropdown = self.driver.find_element(By.ID, "Market")
    dropdown.find_element(By.XPATH, "//option[. = 'Mexican']").click()
    self.driver.find_element(By.ID, "Market").click()
    self.driver.find_element(By.ID, "Scheme").click()
    dropdown = self.driver.find_element(By.ID, "Scheme")
    dropdown.find_element(By.XPATH, "//option[. = 'Momentum']").click()
    self.driver.find_element(By.ID, "Scheme").click()
    self.driver.find_element(By.ID, "Sede").click()
    dropdown = self.driver.find_element(By.ID, "Sede")
    dropdown.find_element(By.XPATH, "//option[. = 'Softtek Guadalajara']").click()
    self.driver.find_element(By.ID, "Sede").click()
    self.driver.find_element(By.ID, "TotalVacationDays").click()
    self.driver.find_element(By.ID, "nextBtn").click()
    self.driver.find_element(By.ID, "projects").click()
    dropdown = self.driver.find_element(By.ID, "projects")
    dropdown.find_element(By.XPATH, "//option[. = 'test']").click()
    assert self.driver.switch_to.alert.text == "Set the percentage %"
    alert = self.driver.switch_to.alert
    alert.send_keys("100")
    alert.accept()
    self.driver.find_element(By.ID, "nextBtn").click()
    self.driver.find_element(By.ID, "badge").click()
    dropdown = self.driver.find_element(By.ID, "badge")
    dropdown.find_element(By.XPATH, "//option[. = 'test level 1']").click()
    self.driver.find_element(By.ID, "badge").click()
    self.driver.find_element(By.ID, "nextBtn").click()
    self.driver.find_element(By.ID, "training").click()
    dropdown = self.driver.find_element(By.ID, "training")
    dropdown.find_element(By.XPATH, '//*[@id="trainingTraining 1"]').click()
    self.driver.find_element(By.ID, "training").click()
    self.driver.find_element(By.ID, "nextBtn").click()
    assert self.driver.find_element_by_class_name("alert-success").is_displayed
  
  def test_CollaboratorsPlatforms(self):
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-dropdown:nth-child(4) > a > span").click()
    self.driver.find_element(By.CSS_SELECTOR, ".active li:nth-child(2) span").click()
    assert self.driver.find_element_by_xpath('/html/body/div[2]/main/div/div[1]/div/h3').is_displayed

  def test_CrearYBorrarCertificado(self):
    self.driver.find_element(By.CSS_SELECTOR, ".sidebar-dropdown:nth-child(4) > a > span").click()
    self.driver.find_element(By.LINK_TEXT, "Certifications").click()
    self.driver.find_element(By.CSS_SELECTOR, ".contenido > .btn").click()
    self.driver.find_element(By.ID, "btn1").click()
    self.driver.find_element(By.ID, "inp1").click()
    self.driver.find_element(By.ID, "inp1").send_keys("test1")
    self.driver.find_element(By.ID, "inp2").click()
    self.driver.find_element(By.ID, "inp2").send_keys("test1")
    self.driver.find_element(By.ID, "inp3").click()
    self.driver.find_element(By.ID, "inp3").send_keys("12121999")
    self.driver.find_element(By.ID, "inp4").click()
    self.driver.find_element(By.ID, "inp4").send_keys("12122020")
    self.driver.find_element(By.ID, "Colaborator").click()
    dropdown = self.driver.find_element(By.ID, "Colaborator")
    dropdown.find_element(By.XPATH, "//option[. = 'test1 test1']").click()
    self.driver.find_element(By.ID, "Colaborator").click()
    self.driver.find_element(By.ID, "Register").click()
    time.sleep(2)  
    action = ActionChains(self.driver)
    firstLevelMenu = self.driver.find_element_by_xpath('//*[@id="tableCollaborators"]')
    action.move_to_element(firstLevelMenu).perform() 
    self.driver.find_element_by_xpath('//*[@id="opt"]/a[1]').click()  
    assert self.driver.switch_to.alert.text == "¿ESTA SEGURO QUE DESEA ELIMINAR ESTOS DATOS DE FORMA PERMANENTE? "
    self.driver.switch_to.alert.accept()
    assert self.driver.title == "Coelens"


  def test_OnbroardingLink(self):
    self.driver.find_element(By.LINK_TEXT, "Collaborators").click()
    self.driver.find_element(By.LINK_TEXT, "OnBoarding").click()
    self.driver.find_element(By.ID, "pendCert-tab").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "number 10").click()
    self.vars["win8825"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win8825"])
    assert self.driver.title == "Log in to continue - Log in with Atlassian account" 

  def test_OffboardingLink(self):
    self.driver.find_element(By.LINK_TEXT, "Collaborators").click()
    self.driver.find_element(By.LINK_TEXT, "OffBoarding").click()
    self.driver.find_element(By.ID, "pendCert-tab").click()
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "number 1").click()
    self.vars["win9010"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win9010"])
    assert self.driver.title == "Log in to continue - Log in with Atlassian account" 
  

  def test_trainingTabs(self):
    self.driver.find_element(By.LINK_TEXT, "Collaborators").click()
    self.driver.find_element(By.LINK_TEXT, "Trainings").click()
    self.driver.find_element(By.ID, "pendCert-tab").click()
    

  # GDCs ---------------------------------------------------------------------------------------------------
  def test_UpdateGdc(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    self.driver.find_element(By.LINK_TEXT, "Update GDCs").click()
    
  
  def test_Aguascalientes(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[2]/a').click()

  def test_Ensenada(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[3]/a').click()

  def test_Eugenia(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[4]/a').click()

  def test_Guadalajara(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[5]/a').click()

  def test_Monterrey(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[6]/a').click()

  def test_Polanco(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    time.sleep(1)
    keyboard.press_and_release('page down')
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[7]/a').click()
    

  def test_Reforma(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    time.sleep(1)
    keyboard.press_and_release('page down')
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[8]/a').click()

  def test_Toreo(self):
    self.driver.find_element(By.LINK_TEXT, "GDCs").click()
    time.sleep(1)
    keyboard.press_and_release('page down')
    time.sleep(1)
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[5]/div/ul/li[9]/a').click()

#  Dashboards ------------------------------------------------------------------------------------------
  def test_DashboardBoardCloud(self):
    self.driver.find_element(By.LINK_TEXT, "Dashboards").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[6]/div/ul/li[1]/a').click()

  def test_DashboardToolDevOps(self):
    self.driver.find_element(By.LINK_TEXT, "Dashboards").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[6]/div/ul/li[2]/a').click()

  def test_DashboardBoardToolAllCenters(self):
    self.driver.find_element(By.LINK_TEXT, "Dashboards").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[6]/div/ul/li[3]/a').click()

  def test_DashboardBoardProjects(self):
    self.driver.find_element(By.LINK_TEXT, "Dashboards").click()
    self.driver.find_element_by_xpath('//*[@id="sidebar"]/div[2]/div[2]/ul/li[6]/div/ul/li[4]/a').click()
  
  # Grafana -----------------------------------------------------------------------------------------------
  def test_GrafanaLink(self):
    self.vars["window_handles"] = self.driver.window_handles
    self.driver.find_element(By.LINK_TEXT, "Grafana").click()
    self.vars["win9010"] = self.wait_for_window(2000)
    self.driver.switch_to.window(self.vars["win9010"])
    assert self.driver.title == "Grafana" 