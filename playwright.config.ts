import { defineConfig, devices } from '@playwright/test';
import dotenv from 'dotenv';
dotenv.config();

const token = process.env.TOKEN;

export default defineConfig({
  timeout: 210 * 1000,
  testDir: './tests',
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: 0,
  workers: 1,
  use: {
    trace: 'on-first-retry',
    extraHTTPHeaders: {
      'Authorization': token,
    }
  },

  projects: [
    {
      name: 'chromium',
      use: { ...devices['Desktop Chrome'] },
    },
  ],
});
