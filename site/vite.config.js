// vite.config.js

import { defineConfig } from 'vite';

export default defineConfig({
  server: {
    host: '127.0.0.1',
    port: 8002,
  },
  build: {
    outDir: 'staticfiles',
  },
});
