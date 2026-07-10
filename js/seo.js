/**
 * seo.js - Módulo para actualizar las etiquetas meta de SEO dinámicamente
 */

const SEO = {
  updateMeta(post, currentUrl) {
    // Si viene el objeto SEO avanzado, úsalo, sino usa fallback básico
    const title = post.seo?.metaTitle || `${post.titulo} | +COTAS`;
    const description = post.seo?.metaDescription || post.descripcion;
    const image = post.imagen;
    const url = currentUrl;

    // Title
    document.title = title;

    // Metas básicas
    this.setMetaContent('name="description"', description);

    // Open Graph / Facebook
    this.setMetaContent('property="og:title"', title);
    this.setMetaContent('property="og:description"', description);
    this.setMetaContent('property="og:image"', image);
    this.setMetaContent('property="og:url"', url);

    // Twitter
    this.setMetaContent('name="twitter:title"', title);
    this.setMetaContent('name="twitter:description"', description);
    this.setMetaContent('name="twitter:image"', image);
    
    // Canonical
    let canonical = document.querySelector('link[rel="canonical"]');
    if (!canonical) {
      canonical = document.createElement('link');
      canonical.setAttribute('rel', 'canonical');
      document.head.appendChild(canonical);
    }
    canonical.setAttribute('href', url);
  },

  setMetaContent(selector, content) {
    let meta = document.querySelector(`meta[${selector}]`);
    if (!meta) {
      meta = document.createElement('meta');
      const attrMatch = selector.split('=');
      meta.setAttribute(attrMatch[0], attrMatch[1].replace(/"/g, ''));
      document.head.appendChild(meta);
    }
    meta.setAttribute('content', content);
  }
};

export default SEO;
