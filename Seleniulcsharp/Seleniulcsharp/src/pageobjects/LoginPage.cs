using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Seleniulcsharp.src.pageobjects
{
    internal class LoginPage
    {
        public void enter_email_address(IWebDriver driver, string emailAddress)
        {
            driver.FindElement(By.Id("validateEmail")).Click();
            driver.FindElement(By.Id("validateEmail")).Clear();
            driver.FindElement(By.Id("validateEmail")).SendKeys(emailAddress);
            driver.FindElement(By.Id("validateForm")).Submit();
        }

        public void enter_password(IWebDriver driver, string password)
        {
            driver.FindElement(By.Id("password")).Clear();
            driver.FindElement(By.Id("password")).SendKeys(password);
            driver.FindElement(By.CssSelector("#loginAndCheckoutButton > div.text")).Click();
        }
    }
}
