using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using Seleniulcsharp.src.pageobjects;
using System;
using Xunit;


namespace Seleniulcsharp
{
    public class UnitTest1
    {
        IWebDriver driver;
        string base_url = "https://sap-sta.paws.com/";

        #region Page object items
        NavBar navBar = new NavBar();
        LoginPage loginPage = new LoginPage();
        #endregion

        public UnitTest1()
        {
            driver = new ChromeDriver(@"C:\SeleniumProjects\WebDrivers\");
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);
            driver.Manage().Window.FullScreen();
            //driver.create_options();
        }

        [Fact]
        public void Test1()
        {
            driver = new ChromeDriver(@"C:\SeleniumProjects\WebDrivers\");
            driver.Manage().Timeouts().ImplicitWait = TimeSpan.FromSeconds(10);

            driver.Url = "http://www.google.co.in";
        }


        [Fact]
        public void test_unknownEmailsGoesToCreateAccount()
        {
            var email_prefix = "unknownEmailAddress";
            var domain = "@inbox.mailtrap.io";

            driver.Url  = base_url;

            navBar.navigate_to_login(driver);
            loginPage.enter_email_address(driver, email_prefix + domain);

            Assert.Contains("Create an account", driver.PageSource);
        }

        [Fact]
        public void test_LoginBadPassword()
        {
            var email_prefix = "705d2182d0-b54e92";
            var domain = "@inbox.mailtrap.io";
            var password = "badpassword";

            driver.Url = base_url;

            navBar.navigate_to_login(driver);
            loginPage.enter_email_address(driver, email_prefix + domain);
            loginPage.enter_password(driver, password);

            Assert.Contains("Your email address or password was incorrect.", driver.PageSource);
        }

        [Fact]
        public void test_CanSignIn()
        {
            var email_prefix = "705d2182d0-b54e92";
            var domain = "@inbox.mailtrap.io";
            var password = "S3l3n1umTest$$";

            driver.Url = base_url;

            navBar.navigate_to_login(driver);
            loginPage.enter_email_address(driver, email_prefix + domain);
            loginPage.enter_password(driver, password);

            Assert.DoesNotContain("Your email address or password was incorrect.", driver.PageSource);
         }

        [Fact]
        public void test_NavigateFavoriates()
        {
            driver.Url = base_url;

            navBar.navigate_to_favoriates(driver);
        }

        [Fact]
        public void test_EnterSearch()
        {
            driver.Url = base_url;

            navBar.add_text_to_search(driver, "hills");

            Assert.Contains("Product Matches", driver.PageSource);
       }

    }
}