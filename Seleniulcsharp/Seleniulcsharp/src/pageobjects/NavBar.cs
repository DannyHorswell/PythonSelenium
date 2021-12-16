using OpenQA.Selenium;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;

namespace Seleniulcsharp.src.pageobjects
{
    public class NavBar
    {
        public void navigate_to_login(IWebDriver driver)
        {
            driver.FindElement(By.CssSelector("button.cookieMessage__button.btn.btn-primary")).Click();
            driver.FindElement(By.CssSelector("a.ico-user.paws-ico.paws-loaded")).Click();
            driver.FindElement(By.Id("signin")).Click();
        }

        public void navigate_to_favoriates(IWebDriver driver)
        {
            driver.FindElement(By.ClassName("ico-favourite")).Click();
        }

        public void navigate_to_basket(IWebDriver driver)
        {
            driver.FindElement(By.ClassName("ico-basket")).Click();
        }

        public void add_text_to_search(IWebDriver driver, string search_text)
        {
            driver.FindElement(By.ClassName("search-input")).Clear();
            driver.FindElement(By.ClassName("search-input")).SendKeys(search_text);
            OpenQA.Selenium.Support.UI.WebDriverWait

            wait = new WebDriverWait(driver, TimeSpan.FromSeconds(5));
            wait.Until(ExpectedConditions.PresenceOfAllElementsLocatedBy(By.XPath("//*[@class='product-matches'][contains(@style, 'display: block;')]")));
        }
    }
}
