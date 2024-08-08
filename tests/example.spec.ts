import { test, Page } from '@playwright/test';

test('poxuy', async ({ page }) => {
  await page.goto('https://jabka.skin/uk/jab-tap');
  await clickUntilZero(page);
});

async function clickUntilZero(page: Page) {
  const currentCount = await page.locator('.energy__string span').textContent();
  let num;
  if (currentCount) {
      const numericString = currentCount.replace(/\s+/g, '');
      const number = parseFloat(numericString);
      num = isNaN(number) ? null : number;
  }
  while (num > 0) {
    await page.locator('.tapper__circle').first().click();
    num--;
  }
}

