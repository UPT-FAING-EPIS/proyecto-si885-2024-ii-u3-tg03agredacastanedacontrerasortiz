provider "azurerm" {
  features {}
  subscription_id = "54362dcc-27cd-4696-b31a-d5d67a72a906"
}

resource "azurerm_resource_group" "rg" {
  name     = "inteligencia-negocios"
  location = "East US"
}

resource "azurerm_mssql_server" "sql_server" {
  name                         = "bi-segunda-unidad"
  resource_group_name          = azurerm_resource_group.rg.name
  location                     = azurerm_resource_group.rg.location
  version                      = "12.0"
  administrator_login          = "adminsql"
  administrator_login_password = "Upt2024!"
}

resource "azurerm_mssql_database" "sql_db" {
  name     = "CICLO_UNIVERSITARIO"
  server_id = azurerm_mssql_server.sql_server.id
  sku_name  = "GP_S_Gen5_2"  
  max_size_gb = 32
  auto_pause_delay_in_minutes = 60  
  min_capacity = 0.5         
}


resource "azurerm_service_plan" "app_service_plan" {
  name                = "ASP-inteligencianegocios-b3b4"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  os_type             = "Linux"
  sku_name            = "B1"
}

resource "azurerm_app_service" "web_app" {
  name                = "UploadCSV-unique123"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  app_service_plan_id = azurerm_service_plan.app_service_plan.id

  site_config {
    linux_fx_version = "DOCKER|alvarocontreras13/uploadcsv-app:v1"
  }
}
