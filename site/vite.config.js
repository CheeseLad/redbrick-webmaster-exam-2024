// vite.config.js

import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    port: 8002,
  },
  build: {
    outDir: 'staticfiles',
  },
});
